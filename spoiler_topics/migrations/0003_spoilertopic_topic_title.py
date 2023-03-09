# Generated by Django 4.1.3 on 2022-11-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiler_topics', '0002_spoilertopic_netflix_id_spoilertopic_no_vote_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spoilertopic',
            name='topic_title',
            field=models.CharField(choices=[('C000', 'Please choose a topic from the list:'), ('C001', 'Does a horse die?'), ('C002', 'Does the dog die?'), ('C003', 'Are animals abused?'), ('C004', 'Does a pet die?'), ('C005', 'Is there dog fighting?'), ('C006', 'Are there bugs?'), ('C007', 'Is there a dead animal?'), ('C008', 'Does a dragon die?'), ('C009', 'Does an animal die? (besides a dog, cat or horse)'), ('C010', 'Are there snakes?'), ('C011', 'Are there spiders?'), ('C012', 'Does a cat die?'), ('C013', 'Is someone gaslighted?'), ('C014', 'Is someone stalked?'), ('C015', 'Is a child abused?'), ('C016', 'Is there domestic violence?'), ('C017', 'Does someone abuse alcohol?'), ('C018', 'Is there addiction?'), ('C019', 'Does someone use drugs?'), ('C020', 'Is someone restrained?'), ('C021', 'Is there excessive gore?'), ('C022', 'Is there shaving/cutting?'), ('C023', 'Are any teeth damaged?'), ('C024', 'Is there genital trauma/mutilation?'), ('C025', 'Is there cannibalism?'), ('C026', 'Is someone crushed to death?'), ('C027', 'Is someone burned alive?'), ('C028', 'Is there amputation?'), ('C029', 'Does a head get squashed?'), ('C030', 'Is someone buried alive?'), ('C031', 'Is there finger/toe mutilation?'), ('C032', 'Is there Achilles Tendon injury?'), ('C033', 'Is there a hanging?'), ('C034', 'Is there eye mutilation?'), ('C035', 'Does someone struggle to breathe?'), ('C036', 'Does someone have a seizure?'), ('C037', 'Is someone tortured?'), ('C038', 'Does someone asphyxiate?'), ('C039', 'Does someone fall to their death?'), ('C040', 'Does someone break a bone?'), ('C041', 'Does someone fall down stairs?'), ('C042', 'Is an infant abducted?'), ('C043', 'Does a kid die?'), ('C044', 'Is the R word used?'), ('C045', 'Does someone overdose?'), ('C046', 'Is someone kidnapped?'), ('C047', 'Does a parent die?'), ('C048', "Is a child's toy destroyed?"), ('C049', 'Does someone cheat?'), ('C050', 'Are there clowns?'), ('C051', 'Are there jumpscares?'), ('C052', 'Is someone possessed?'), ('C053', 'Is there a shower scene?'), ('C054', 'Are there ghosts?'), ('C055', 'Does someone wet/soil themselves?'), ('C056', 'Does someone vomit?'), ('C057', 'Does someone fart or spit?'), ('C058', 'Is there audio gore?'), ('C059', 'Are there 9/11 depictions?'), ('C060', 'Is there copaganda?'), ('C061', 'Is electro-therapy used?'), ('C062', 'Is there a mental institution scene?'), ('C063', 'Is there a hospital scene?'), ('C064', 'Does someone have cancer?'), ('C065', 'Are needles/syringes used?'), ('C066', 'Are there anxiety attacks?'), ('C067', 'Does someone suffer from PTSD?'), ('C068', 'Does someone have an eating disorder?'), ('C069', 'Does someone die by suicide?'), ('C070', 'Is there misophonia?'), ('C071', 'Is there body dysmorphia?'), ('C072', 'Is there autism specific abuse?'), ('C073', 'Is there a claustrophobic scene?'), ('C074', 'Does someone attempt suicide?'), ('C075', 'Does someone say "I\'ll kill myself"?'), ('C076', 'Does someone self harm?'), ('C077', 'Is a mentally ill person violent?'), ('C078', 'Is there shakey cam?'), ('C079', 'Does a baby cry?'), ('C080', 'Are there flashing lights or images?'), ('C081', 'Is the fourth wall broken?'), ('C082', 'Does someone miscarry?'), ('C083', 'Is a baby stillborn?'), ('C084', 'Is there childbirth?'), ('C085', 'Are there babies or unborn children?'), ('C086', 'Does a pregnant woman die?'), ('C087', 'Are there abortions?'), ('C088', 'Does an LGBT person die?'), ('C089', 'Are there n-words?'), ('C090', 'Are there "Man in a dress" jokes?'), ('C091', 'Is there hate speech?'), ('C092', 'Are there fat jokes?'), ('C093', 'Is there ableist language or behavior?'), ('C094', 'Does the black guy die first?'), ('C095', 'Are there homophobic slurs?'), ('C096', 'Is someone misgendered?'), ('C097', 'Is there antisemitism?'), ('C098', 'Is there a large age gap?'), ('C099', 'Are there nude scenes?'), ('C100', 'Is someone sexually objectified?'), ('C101', 'Is there sexual content?'), ('C102', 'Are there incestuous relationships?'), ('C103', 'Is someone sexually assaulted?'), ('C104', 'Is a male character ridiculed for crying?'), ('C105', 'Does someone have a stroke?'), ('C106', 'Is someone homeless?'), ('C107', 'Is Santa (et al) spoiled?'), ('C108', 'Does it have a sad ending?'), ('C109', 'Does a plane crash?'), ('C110', 'Does a car honk or tires screech?'), ('C111', 'Does a car crash?'), ('C112', 'Is someone hit by a car?'), ('C113', 'Is there blood/gore?'), ('C114', 'Does someone drown?'), ('C115', 'Is there a nuclear explosion?'), ('C116', 'Is there gun violence?')], default='C000', max_length=4),
        ),
    ]